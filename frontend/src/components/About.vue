<template>
    <div>
        <p>About</p>
        <div>
            <label><b>{{ msg }}</b></label>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      msg: ""
    };
  },
  created() {
    this.getMessage();
  },
  methods: {
    getMessage() {
      const path = `/api/about`;
      axios
        .get(path)
        .then(response => {
          this.msg = response.data.message;
        })
        .catch(error => {
          this.msg = "Error.";
        });
    }
  }
};
</script>