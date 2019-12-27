import {
    DataHelper
} from "@/common/helpers";

import ApiService from "@/common/api.service";
import {
    FETCH_PERSONS,
    UPDATE_PERSON,
    GET_PERSON,
    CREATE_PERSON,
} from "./actions.type";
import {
    SET_PERSONS,
    SET_PERSON,
} from "./mutations.type";

export const state = {
    persons: [],
};
const getters = {
    persons(state) {
        return state.persons;
    },
};
export const actions = {
    [FETCH_PERSONS](context,force = false) {
        if (context.state.persons.length == 0 || force) {
            ApiService.setHeader();
            return ApiService.query("persons",{})
                .then(({
                    data
                }) => {
                    context.commit(SET_PERSONS, data);
                    return data;
                })
                .catch(error => {
                    throw new Error(error);
                });
        } else {
            return Promise.resolve(context.state.persons);
        }
    },
    [GET_PERSON](context, id) {
            ApiService.setHeader();
        return ApiService.get("persons",id)
            .then(({
                data
            }) => {
                context.commit(SET_PERSON, data);
                return data;
            });
    },
    [UPDATE_PERSON](context, {
        id,
        data
    }) {
            ApiService.setHeader();
        return ApiService.update("persons",id, data)
            .then(({
                data
            }) => {
                context.commit(SET_PERSON, data);
                    return data;
            });
    },
    [CREATE_PERSON](context, {
        data
    }) {
            ApiService.setHeader();
        return ApiService.post("persons/",data)
            .then(({
                data
            }) => {
                context.commit(SET_PERSON, data);
                    return data;
            });
    },

};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
    [SET_PERSONS](state, persons) {
        state.persons = persons;
    },
    [SET_PERSON](state, person) {
        if('id' in person)
        {
            DataHelper.updateById(state.persons, person)
        }
    },
};

export default {
    state,
    actions,
    mutations,
    getters
};
