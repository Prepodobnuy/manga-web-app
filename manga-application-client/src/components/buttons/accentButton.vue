<script>
export default {
    name: "accentButton",
    props: {
        title: String
    }
}
</script>

<template>
    <button class="button-bg"> {{ title }} </button>
</template>

<style lang="scss" scoped>
button.button-bg {
    outline: unset;
    border: unset;
    width: 100%;
    padding: 0px 4px;
    height: 36px;
    border-radius: 4px;
    font-size: 1.5ch;
    font-weight: 500;
    -webkit-box-shadow: 0px 2px 6px 0px var(--shadow-color);
    -moz-box-shadow: 0px 2px 6px 0px var(--shadow-color);
    box-shadow: 0px 2px 6px 0px var(--shadow-color);
    transition: background-color 0.2s, padding 0.2s;
    background-color: var(--accent-color);
    color: var(--font-color);

    &:hover {
        background-color: var(--accent-color-hover);
    }
}
</style>