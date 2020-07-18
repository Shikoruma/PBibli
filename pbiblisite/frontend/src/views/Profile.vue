<template>
  <div class="card">
    <div class="card-header">
      <h3>Votre profile</h3>
    </div>
    <div class="card-body">
      <form id="editor-form" class="form">
        <div class="form-group">
          <label>Nom utilisateur</label
          ><input
            class="form-control"
            type="text"
            v-model="authUser.username"
            readonly
          />
        </div>
        <div class="form-group">
          <label>Prénom</label
          ><input
            class="form-control"
            type="text"
            v-model="authUser.first_name"
          />
        </div>
        <div class="form-group">
          <label>Nom</label
          ><input
            class="form-control"
            type="text"
            v-model="authUser.last_name"
          />
        </div>
        <div class="form-group">
          <label>Email</label
          ><input class="form-control" type="email" v-model="authUser.email" />
        </div>
        <template>
          <div class="text-success" v-show="goodpassword">
            Le mot de passe a été modifié
          </div>
          <div class="text-danger" v-show="goodpassword == false">
            Le mot de passe est incorrect
          </div>
          <div class="text-danger" v-show="!passvalid">
            L'ancien mot de passe est nécéssaire pour changer celui-ci
          </div>
          <div class="text-danger" v-show="!passvalid">
            Le nouveau mot de passe est nécéssaire
          </div>
          <div class="text-danger" v-show="!passvalid">
            Le nouveau mot de passe et la confirmation doivent être identiques
          </div>
          <div class="form-group">
            <label>Password</label>
            <input
              v-model="form.old_password"
              type="password"
              class="form-control"
            />
          </div>
          <div class="form-group">
            <label> New password</label>
            <input
              v-model="form.new_password"
              type="password"
              class="form-control"
            />
          </div>
          <div class="form-group">
            <label>Confirm new password</label>
            <input
              v-model="form.new_password2"
              type="password"
              class="form-control"
            />
          </div>
        </template>
        <div class="btn-group" role="group">
          <button class="btn btn-primary" type="button" @click="update">
            Modifier
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import { showMsgOk } from "@/components/Modal";
import { UPDATE_AUTHUSER, UPDATE_PASSWORD } from "@/store/actions.type";
import { mapGetters } from "vuex";
export default {
  name: "Profile",
  components: {},
  data() {
    return {
      goodpassword: null,
      form: {
        old_password: "",
        new_password: "",
        new_password2: ""
      }
    };
  },
  computed: {
    ...mapGetters(["authUser"]),
    passvalid() {
      if (
        this.form.old_password == "" &&
        this.form.new_password == "" &&
        this.form.new_password2 == ""
      )
        return true;
      if (
        (this.form.old_password != "" && this.form.new_password == "") ||
        (this.form.old_password == "" && this.form.new_password != "") ||
        (this.form.new_password == "" && this.form.new_password2 == "")
      )
        return false;
      if (this.form.new_password != this.form.new_password2) return false;
      return true;
    }
  },
  methods: {
    update() {
      this.goodpassword = null;
      if (
        document.querySelector("#editor-form").checkValidity() &&
        this.passvalid != false
      ) {
        if (this.form.old_password != "") {
          this.$store
            .dispatch(UPDATE_PASSWORD, this.form)
            .then(() => {
              this.goodpassword = true;
              this.updateUser();
              this.form.old_password = "";
              this.form.new_password = "";
              this.form.new_password2 = "";
            })
            .catch(e => {
              if (e.response.status == 400) {
                this.goodpassword = false;
                showMsgOk("Mot de passe incorrect");
              }
              // eslint-disable-next-line
              console.log(e.response);
            });
        } else {
          this.updateUser();
        }
      } else {
        document.querySelector("#editor-form").reportValidity();
      }
    },
    updateUser() {
      this.$store.dispatch(UPDATE_AUTHUSER, this.authUser).then(() => {
        showMsgOk("Profile mis à jour");
      });
    }
  }
};
</script>
