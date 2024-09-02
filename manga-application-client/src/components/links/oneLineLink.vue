<script>
export default {
    name: "oneLineLink",
    props: {
        text: String,
        link: String,
    },
    methods: {
        redirect() {
            this.$router.push(this.link);
        }
    }
}
</script>

<template>
    <a :href="link" class="text" target="_blank">{{ text }}</a>
</template>

<style lang="scss" scoped>
.text {
    user-select: none;
    cursor: pointer;
    color: var(--accent-font);
    transition: color 0.1s;

    &:hover {
        color: var(--accent-font-hover);
    }

    &:active {
        color: var(--accent-font-active);
    }
}
</style>