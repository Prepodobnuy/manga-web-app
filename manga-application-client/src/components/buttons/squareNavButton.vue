<script>
export default {
    name: "squareNavButton",
    props: {
        title: String,
        d: String
    }
}
</script>

<template>
    <button class="squareNavButton">
        {{ title }}
        <svg v-if="d" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
            stroke="currentColor" class="size-6">
            <path stroke-linecap="round" stroke-linejoin="round" :d="d" />
        </svg>
    </button>
</template>

<style lang="scss">
button.squareNavButton {
    width: 20px;
    border: unset;
    outline: unset;
    width: fit-content;
    cursor: pointer;
    font-weight: 600;
    padding: 8px;
    border-radius: 4px;
    color: var(--font-color);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: 5px;
    flex-shrink: 0;

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