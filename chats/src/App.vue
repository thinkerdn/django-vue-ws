<template>
  <div>
    <input type="text" v-model="message" />
    <p><input type="button" @click="send" value="send" /></p>
    <p><input type="button" @click="close_socket" value="close" /></p>
  </div>
</template>


<script>
export default {
  name: "websocket1",
  data() {
    return {
      message: "",
      testsocket: "",
    };
  },
  methods: {
    send() {
      this.testsocket.send(this.message);
      this.testsocket.onmessage = (res) => {
        console.log("re", res.data);
      };
    },
    close_socket() {
      this.testsocket.close();
    },
  },
  mounted() {
    try {
      this.testsocket = new WebSocket("ws://127.0.0.1:8000/ws/");
    } catch (err) {
      console.log(err);
    }

    this.testsocket.onmessage = (res) => {
      console.log("message", res.data);
    };
  },
};
</script>