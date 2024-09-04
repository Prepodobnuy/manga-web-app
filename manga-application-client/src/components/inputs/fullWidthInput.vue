<script>

export default {
    name: "fullWidthInput",
    data() {
        return {
            caption: "",
            showPreviewText: true
        }
    },
    props: {
        previewText: String,
        showHints: Boolean,
        hints: Array
    },
    methods: {
        inputHandler() {
            this.caption = this.$refs.input.value;

            if (this.caption === '') {
                this.showPreviewText = true
            } else {
                this.showPreviewText = false
            }
        }
    }
}

</script>

<template>
    <div class="input-wrapper">
        <div v-if="showPreviewText" class="previewText">{{ previewText }}</div>
        <input v-on:input="inputHandler" ref="input" type="text">
        <div v-if="showHints" class="hint-menu"></div>
    </div>
</template>

<style lang="scss" scoped>
.input-wrapper {
    width: 100%;
    position: relative;
    background-color: var(--input-bg-color);
    box-shadow: 0px 0px 0px 1px var(--shadow-color);
    border-radius: 2px;
    padding: 0px 8px;
    height: 28px;

    * {
        color: var(--input-font-color);
    }

    .previewText {
        pointer-events: none;
        position: absolute;
        top: 4px;
        opacity: 0.7;
    }

    input {
        border: unset;
        outline: unset;
        width: 100%;
        height: 100%;
        font-size: medium;
        background-color: var(--input-bg-color);
    }
}
</style>