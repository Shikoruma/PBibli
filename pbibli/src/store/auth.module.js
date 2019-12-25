import ApiService from "@/common/api.service";

import {
  CHECK_AUTH,
} from "./actions.type";
import { SET_AUTH, PURGE_AUTH } from "./mutations.type";

const state = {
  isAuthenticated: false,
};

const getters = {
  isAuthenticated(state) {
    return state.isAuthenticated;
  },
};

const actions = {
 [CHECK_AUTH](context) {
    return new Promise((resolve, reject) => {
      ApiService.query("auth/",{})
        .then(({ data }) => {
      		context.commit(SET_AUTH);
            resolve()
        })
        .catch((e) => {
            if(e.response.status==403)
            {
      			context.commit(PURGE_AUTH);
            }
            resolve()
        });
    });
  },
};

const mutations = {
  [SET_AUTH](state, token) {
    state.isAuthenticated = true;
  },
  [PURGE_AUTH](state) {
    state.isAuthenticated = false;
  }
};

export default {
  state,
  actions,
  mutations,
  getters
};
