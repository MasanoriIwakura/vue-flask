<template>
    <div>
        <p>About</p>
        <div>
            <label><b>{{ msg }}</b></label>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            msg: ''
        }
    },
    created () {
        this.getMessage()
    },
    methods: {
        getMessage () {
            const path = `http://localhost:5000/api/about`
            axios.get(path)
            .then(response => {
                this.msg = response.data.message
            })
            .catch(eror => {
                this.msg = 'Error.'
            })
        }
    }
}
</script>