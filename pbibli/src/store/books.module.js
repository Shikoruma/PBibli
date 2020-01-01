import {
    DataHelper
} from "@/common/helpers";

import ApiService from "@/common/api.service";
import {
    FETCH_BOOKS,
    UPDATE_BOOK,
    GET_BOOK,
    CREATE_BOOK,
    FIND_BOOK,
} from "./actions.type";
import {
    SET_BOOKS,
    SET_BOOK,
} from "./mutations.type";

export const state = {
    books: [],
};
const getters = {
    books(state) {
        return state.books;
    },
};
export const actions = {
    [FETCH_BOOKS](context,force = false) {
        if (context.state.books.length == 0 || force) {
            ApiService.setHeader();
            return ApiService.query("books",{})
                .then(({
                    data
                }) => {
                    context.commit(SET_BOOKS, data);
                    return data;
                })
                .catch(error => {
                    throw new Error(error);
                });
        } else {
            return Promise.resolve(context.state.books);
        }
    },
    [GET_BOOK](context, id) {
            ApiService.setHeader();
        return ApiService.get("books",id)
            .then(({
                data
            }) => {
                context.commit(SET_BOOK, data);
                return data;
            });
    },
    [UPDATE_BOOK](context, {
        id,
        data
    }) {
            ApiService.setHeader();
        return ApiService.update("books",id, data)
            .then(({
                data
            }) => {
                context.commit(SET_BOOK, data);
                    return data;
            });
    },
    [CREATE_BOOK](context, {
        data
    }) {
            ApiService.setHeader();
        return ApiService.post("books/",data)
            .then(({
                data
            }) => {
                context.commit(SET_BOOK, data);
                    return data;
            });
    },
    [FIND_BOOK](context, isbn) {
            ApiService.setHeader();
        return ApiService.post("books/find_book/",{'isbn':isbn})
            .then(({
                data
            }) => {
                return data;
            });
    },

};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
    [SET_BOOKS](state, books) {
        state.books = books;
    },
    [SET_BOOK](state, book) {
        if('id' in book)
        {
            DataHelper.updateById(state.books, book)
        }
    },
};

export default {
    state,
    actions,
    mutations,
    getters
};
