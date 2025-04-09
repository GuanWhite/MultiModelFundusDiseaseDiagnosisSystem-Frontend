<template>
  <div id="app" style="width: auto;">
    <app-header></app-header>
    <app-content></app-content>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from "./components/Header";
import Footer from "./components/Footer";
import Content from "./components/Content";
export default {
  name1: "“X-eyes”智慧眼疾检测",
  name: "病理性近视病灶检测与分割系统",
  data() {
    return {};
  },
  components: {
    "app-header": Header,
    "app-footer": Footer,
    "app-content": Content,
  },
  methods: {},
};
</script>

<style scope="this api replaced by slot-scope in 2.5.0+">
</style>
