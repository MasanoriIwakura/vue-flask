<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Links</h2>
    <ul>
      <li>
        <router-link to="about">About</router-link>
      </li>
      <li>
        <router-link to="todo">Todo</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Flask × Vue.js App'
    }
  }
}
</script>