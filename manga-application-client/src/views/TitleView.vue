<script>
import axios from 'axios'

export default {
    name: "TitleView",
    data() {
        return {
            id: this.$route.params.id,
            data: null
        }
    },
    methods: {
        fetchData() {
            axios.get(`/title/data/${this.id}`)
                .then(response => response.json())
                .then(data => {
                    this.data = data
                    console.log('Fetched data:', this.data)
                })
                .catch(error => {
                    console.error('Error fetching data:', error)
                })
        }
    },
    created() {
        this.fetchData()
    }
}

</script>

<template>
    <div class="ViewForm">
        asdasd
        {{ id }}
    </div>
</template>

<style lang="scss" scoped></style>