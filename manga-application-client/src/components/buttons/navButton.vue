<script>
export default {
    name: "navButton",
    props: {
        title: String,
        leftD: String,
        rightD: String
    }
}
// m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z
</script>

<template>
    <button class="navButton fs-default">
        <svg v-if="leftD" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
            stroke="currentColor" class="size-6">
            <path stroke-linecap="round" stroke-linejoin="round" :d="leftD" />
        </svg>
        {{ title }}
        <svg v-if="rightD" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
            stroke="currentColor" class="size-6">
            <path stroke-linecap="round" stroke-linejoin="round" :d="rightD" />
        </svg>
    </button>
</template>

<style lang="scss">
button.navButton {
    border: unset;
    outline: unset;
    width: fit-content;
    cursor: pointer;
    font-weight: 600;
    padding: 8px 6px;
    border-radius: 4px;
    color: var(--font-color);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: 5px;

    svg {
        width: 20px;
        height: 20px;
        stroke: var(--font-color);
    }

    background-color: var(--inactive-font-color);
    transition: transform 0.2s,
    background-color 0.2s;

    &:hover {
        background-color: var(--inactive-font-color-hover);
    }

    &:active {
        transform: translateY(2px);
        background-color: var(--inactive-font-color-active);
    }
}
</style>