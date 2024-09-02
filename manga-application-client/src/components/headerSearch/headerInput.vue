<script>
export default {
    name: "headerSearch",
    props: {
        previewText: String
    },
    data() {
        return {
            viewPreviewText: true,
            text: "",
        }
    },
    methods: {
        inputHandler() {
            this.text = this.$refs.input.value;
            this.$emit('input-change')

            if (this.text == '') {
                this.viewPreviewText = true
            } else {
                this.viewPreviewText = false
            }
        }
    }
}
</script>

<template>
    <div class="input-bg">
        <div v-if="viewPreviewText" class="previewtext">
            {{ previewText }}
        </div>
        <input v-on:input="inputHandler" ref="input" type="text">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="size-6">
            <path stroke-linecap="round" stroke-linejoin="round"
                d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
        </svg>

    </div>
</template>

<style lang="scss" scoped>
.input-bg {
    width: 100%;
    height: 36px;
    position: relative;
    background-color: var(--input-bg-color);
    border-radius: 4px;
    -webkit-box-shadow: 0px 2px 6px 0px var(--shadow-color);
    -moz-box-shadow: 0px 2px 6px 0px var(--shadow-color);
    box-shadow: 0px 2px 6px 0px var(--shadow-color);
    display: flex;

    .previewtext {
        pointer-events: none;
        position: absolute;
        top: 50%;
        left: 4px;
        transform: translate(0, -50%);
        font-size: 1.6ch;
    }

    input {
        outline: unset;
        border: unset;
        width: 100%;
        padding-left: 4px;
        padding-right: 4px;
        background-color: unset;
        height: 36px;
        font-size: 1.6ch;
    }

    svg {
        width: 26px;
        stroke: var(--font-color);
        padding-right: 4px;
        flex-shrink: 0;
        transition: transform 0.2s;

        &:hover {
            transform: scale(1.1);
        }

        &:active {
            transform: scale(0.95);
        }
    }
}
</style>