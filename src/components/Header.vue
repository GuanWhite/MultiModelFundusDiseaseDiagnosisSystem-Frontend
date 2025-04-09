<template>
  <div id="Header">
    
    <div id="word">
      <h1>{{ msg }}</h1>
      <h3>{{subtitle}}</h3>
    </div>
    
  </div>
</template>
<script>
export default {
  name: "Header",
  data() {
    return {
      msg: "病理性近视病灶检测与分割系统",
      msg1: "X-eyes 智慧眼疾检测",
      subtitle: "Fundus Color Photo Disc Detection And Segmentation System",
      subtitle1: "X-eyes Intelligent Eye Disease Detection",
      activeIndex: "1",
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>
<style scoped>
#Header {
  /* padding: 30px 110px 0 150px; */
  padding: 15px 0 0 0;
  width: 100%;
  height: 80px;
  margin: 10px auto;
}

#word {
  /* margin-left: 45%; */
  margin-top: -35px;
  margin-bottom: 30px;
  height: 60px;
  line-height: 3.2em;
  padding-left: 324px;
}

h1 {
  /*text-align: center;*/
  color: #67abd6;
  letter-spacing: 3px;
  font-size: 2.3em;
  margin-bottom: 0px;
}
h3 {
  /*text-align: center;*/
  color: #67abd6;
  letter-spacing: 3px;
  /* font-size: 2.3em; */
  /* height: 30px; */
  margin-top: 0px;
}

.el-menu-demo {
  width: 80%;
  margin: 0px auto;
  padding: 0px auto;
}

.top-left-edition span i {
  float: left;
  margin-right: 10px;
}

i,
input,
label {
  vertical-align: middle;
}

i {
  border: 0;
  display: block;
  cursor: pointer;
}

.top-left-edition span {
  float: left;
  font-size: 16px;
  color: #999999;
  line-height: 24px;
  margin-right: 40px;
}
</style>


