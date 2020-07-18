import createCrud from "@/common/storeCrudHelper";

const users_extra = {
  state: {},
  getters: {},
  actions: {},
  mutations: {}
};
const users = createCrud("users", users_extra);
export default users;
