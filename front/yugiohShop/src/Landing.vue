<template>
  <div id="landing">
    <sidebar class="sidebar"/>
    <div class="main">
      <img src="http://uploads1.yugioh.com/character/4/detail/detail/solomon-l.png?1375717041">
      <h1>{{ msg }}</h1>
    </div>    
  </div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Welcome to Grandpa\'s Yugioh cards store!'
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#landing {
  display: flex;
}

.sidebar {
  order: 1;
	flex: 1;
}

.main {
  order: 1;
  flex: 1;
}

h1, h2 {
  font-weight: normal;
}
</style>
