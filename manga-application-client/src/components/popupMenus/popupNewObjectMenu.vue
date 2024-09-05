<script>
import navButton from '@/components/buttons/navButton.vue';
import LineSplitter from './LineSplitter.vue';

export default {
    name: "popupNewObjectMenu",
    components: {
        navButton,
        LineSplitter
    },
    data() {
        return {
            fields: [
                { title: 'Добавить тайтл', link: '/create/title' },
                { title: 'Добавить автора', link: '/create/author' },
                { title: 'Добавить художника', link: '/create/artist' },
                { title: 'Добавить издательство', link: '/create/publisher' },
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
        <LineSplitter />
        <navButton class="row" title="Мои добавления" @click="redirect('/create')" />
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