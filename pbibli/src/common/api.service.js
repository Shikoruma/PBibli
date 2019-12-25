import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import JwtService from "@/common/jwt.service";
import {
    API_URL
} from "@/common/config";

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

var csrftoken = readCookie('csrftoken');

const ApiService = {
    init() {
        Vue.use(VueAxios, axios);
        Vue.axios.defaults.baseURL = API_URL;
    },

    setHeader() {
        if(readCookie('csrftoken')!=null){
        Vue.axios.defaults.headers.common[
            "X-CSRFToken"
        ] = readCookie('csrftoken');
        }
    },

    query(resource, params) {
        return Vue.axios.get(resource, params)
    },

    get(resource, slug = "") {
        return Vue.axios.get(`${resource}/${slug}`)
    },

    post(resource, params) {
        return Vue.axios.post(`${resource}`, params);
    },

    update(resource, slug, params) {
        return Vue.axios.patch(`${resource}/${slug}/`, params);
    },

    put(resource, params) {
        return Vue.axios.put(`${resource}`, params);
    },

    delete(resource, slug = "") {
        return Vue.axios.delete(`${resource}/${slug}`)
    }
};

export default ApiService;

