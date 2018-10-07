<template>
    <div>
        <p>Todo List</p>
        <p style="color:red"><b>{{ errMsg }}</b></p>
        <div>
            <p>New Todo</p>
            <input type="text" v-model="addBody">
            <button @click="addTodo">Add Todo</button>
        </div>
        <ul id="todos">
            <li v-for="todo in todos" :key="todo.id">
                {{ todo.body }}&nbsp;
                <button @click="deleteTodo(todo.id)">Delete</button>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      todos: {},
      errMsg: "",
      addBody: "",
    };
  },
  created() {
    this.getTodos();
  },
  methods: {
    getTodos() {
      const path = `/api/todos`;
      axios
        .get(path)
        .then(response => {
          this.todos = response.data.todos;
        })
        .catch(error => {
          this.errMsg = "Error.";
        });
    },
    addTodo() {
      const path = `/api/todos`;

      if (this.addBody == "") {
        this.errMsg = "TODOを入力してください";
        return;
      }
      axios
        .post(path, {
          body: this.addBody
        })
        .then(response => {
          this.addBody = ''
          this.getTodos();
        });
    },
    deleteTodo(id) {
      const path = `/api/todo/`;
      const params = new URLSearchParams();

      axios
        .delete(path + id)
        .then(response => {
          this.getTodos();
        })
        .catch(error => {
          this.errMsg = "Error.";
        });
    }
  }
};
</script>
