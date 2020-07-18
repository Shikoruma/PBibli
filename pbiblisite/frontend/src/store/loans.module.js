import createCrud from "@/common/storeCrudHelper";

const loans_extra = {
  state: {},
  getters: {},
  actions: {},
  mutations: {}
};
const loans = createCrud("loans", loans_extra);
export default loans;
