<script>
import navButton from '@/components/buttons/navButton.vue';

export default {
    name: "popupNewObjectMenu",
    components: {
        navButton
    },
    data() {
        return {
            fields: [
                { title: 'Добавить тайтл', link: '/create/title' },
                { title: 'Добавить автора', link: '/create/author' },
                { title: 'Мои добавления', link: '/create' },
            ]
        }
    },
    methods: {
        redirect(link) {
            this.$emit('hideAll')
            this.$router.push(link);
        }
    }
}
</script>

<template>
    <div class="popup-menu">
        <navButton v-for="(field, index) in fields" :key="index" :title="field.title" @click="redirect(field.link)"
            class="row" />
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
}
</style>