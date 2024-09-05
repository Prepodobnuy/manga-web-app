<script>
import themeSwitchButton from '../buttons/themeSwitchButton.vue';
import { applyColors, setHue, getHue } from '@/color_funcs';

export default {
    name: "popupColorThemeMenu",
    components: {
        themeSwitchButton
    },
    data() {
        return {
            value: getHue(),
        }
    },
    methods: {
        onInputChange() {
            setHue(this.value)
            applyColors()
        }
    }
}
</script>

<template>
    <div class="popup-menu">
        <themeSwitchButton v-on:click="onInputChange" />
        <div class="slider-container">
            <input type="range" id="slider" min="0" max="360" @input="onInputChange" v-model="value" step="1">
        </div>
    </div>
</template>

<style lang="scss" scoped>
.popup-menu {
    position: absolute;
    width: max-content;
    padding: 4px;
    right: 0;
    top: 52px;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    border-radius: 4px;
    background-color: var(--fg-color);
    -webkit-box-shadow: 0px 2px 6px 0px var(--shadow-color);
    -moz-box-shadow: 0px 2px 6px 0px var(--shadow-color);
    box-shadow: 0px 2px 6px 0px var(--shadow-color);
    font-size: medium;
    gap: 4px;
    height: 40px;

    * {
        flex-shrink: 0;
        height: 100%;
    }

    .slider-container {
        input[type="range"] {
            -webkit-appearance: none;
            appearance: none;
            width: 220px;
            height: 100%;
            padding: 0 0px;
            background: linear-gradient(90deg, #ff0000, #ffff00, #00ff00, #00ffff, #0000ff, #ff00ff, #ff0000);
            border-radius: 2px;
            outline: none;
            overflow: hidden;
        }

        input[type="range"]::-moz-range-thumb {
            box-shadow: 0px 0px 0px 9px var(--fg-color);
            background-color: var(--accent-font);
            border: none;
            border-radius: 2px;
            padding: 3px;
            height: 1px;
            width: 1px;
        }


    }
}
</style>