<script>
import navButton from '@/components/buttons/navButton.vue';

export default {
    name: "popupColorThemeMenu",
    components: {
        navButton
    },
    data() {
        return {
            sliderThumbColor: "#00ffff",
        }
    },
    methods: {
    }
}
</script>

<template>
    <div class="popup-menu">
        <navButton v-for="(field, index) in fields" :key="index" :title="field.title" @click="redirect(field.link)"
            class="row" />
        <div class="slider-container">
            <input type="range" id="slider" min="0" max="360" :style="{}" value="180" step="1">
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
    border-radius: 4px;
    background-color: var(--fg-color);
    -webkit-box-shadow: 0px 2px 6px 0px var(--shadow-color);
    -moz-box-shadow: 0px 2px 6px 0px var(--shadow-color);
    box-shadow: 0px 2px 6px 0px var(--shadow-color);
    font-size: medium;

    .row {
        width: 100%;
        display: flex;
        align-items: flex-start;
        justify-content: flex-start;
    }

    .slider-container {
        input[type="range"] {
            -webkit-appearance: none;
            appearance: none;
            width: 220px;
            height: 29px;
            padding: 0 0px;
            background: linear-gradient(90deg, #ff0000, #ffff00, #00ff00, #00ffff, #0000ff, #ff00ff, #ff0000);
            border-radius: 4px;
            outline: none;
            overflow: hidden;
        }

        input[type="range"]::-moz-range-thumb {
            box-shadow: 0px 0px 0px 2px var(--input-bg-color);
            background-color: transparent;
            border: none;
            border-radius: 0px;
            height: 29px;
            width: 3px;
        }


    }
}
</style>