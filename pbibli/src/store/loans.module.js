import {
    DataHelper
} from "@/common/helpers";

import ApiService from "@/common/api.service";
import {
    FETCH_LOANS,
    UPDATE_LOAN,
    GET_LOAN,
    CREATE_LOAN,
} from "./actions.type";
import {
    SET_LOANS,
    SET_LOAN,
} from "./mutations.type";

export const state = {
    loans: [],
};
const getters = {
    loans(state) {
        return state.loans;
    },
};
export const actions = {
    [FETCH_LOANS](context,force = false) {
        if (context.state.loans.length == 0 || force) {
            ApiService.setHeader();
            return ApiService.query("loans",{})
                .then(({
                    data
                }) => {
                    context.commit(SET_LOANS, data);
                    return data;
                })
                .catch(error => {
                    throw new Error(error);
                });
        } else {
            return Promise.resolve(context.state.loans);
        }
    },
    [GET_LOAN](context, id) {
            ApiService.setHeader();
        return ApiService.get("loans",id)
            .then(({
                data
            }) => {
                context.commit(SET_LOAN, data);
                return data;
            });
    },
    [UPDATE_LOAN](context, {
        id,
        data
    }) {
            ApiService.setHeader();
        return ApiService.update("loans",id, data)
            .then(({
                data
            }) => {
                context.commit(SET_LOAN, data);
                    return data;
            });
    },
    [CREATE_LOAN](context, {
        data
    }) {
            ApiService.setHeader();
        return ApiService.post("loans/",data)
            .then(({
                data
            }) => {
                context.commit(SET_LOAN, data);
                    return data;
            });
    },

};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
    [SET_LOANS](state, loans) {
        state.loans = loans;
    },
    [SET_LOAN](state, loan) {
        if('id' in loan)
        {
            DataHelper.updateById(state.loans, loan)
        }
    },
};

export default {
    state,
    actions,
    mutations,
    getters
};
