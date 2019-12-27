import {
    UsersService,
} from "@/common/api.service";
import ApiService from "@/common/api.service";
import {
    DataHelper
} from "@/common/helpers";


import {
    FETCH_USERS,
    UPDATE_USER,
    GET_USER,
    CREATE_USER
} from "./actions.type";
import {
    SET_USERS,
    SET_USER,
    ADD_USER
} from "./mutations.type";

export const state = {
    users: []
};
const getters = {
    users(state) {
        return state.users;
    }
};
export const actions = {
    [FETCH_USERS](context, force = false) {
        if (context.state.users.length == 0 || force) {
            return UsersService.query({})
                .then(({
                    data
                }) => {
                    context.commit(SET_USERS, data);
                    return data;
                })
                .catch(error => {
                    throw new Error(error);
                });
        } else {
            return Promise.resolve(context.state.users);
        }
    },
    [GET_USER](context, id) {
        return UsersService.get(id)
            .then(({
                data
            }) => {
                context.commit(SET_USER, data);
                return data;
            });
    },
    [UPDATE_USER](context, {
        id,
        data
    }) {
        return UsersService.update(id, data)
            .then(({
                data
            }) => {

                context.commit(SET_USER, data);
                return data;
            });
    },
    [CREATE_USER](context, {
        data
    }) {
        console.log(data)
        return ApiService.post("users/create_user/", data)
            .then(({
                data
            }) => {
                context.commit(SET_USER, data);
                return data;
            });
    }


};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
    [SET_USERS](state, users) {
        state.users = users;
    },
    [SET_USER](state, user) {
        if ('id' in user && state.users.length != 0) {
            DataHelper.updateById(state.users, user)
        }
    },

};

export default {
    state,
    actions,
    mutations,
    getters
};