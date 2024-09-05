<script>
import headerSearch from '@/components/headerSearch/headerInput.vue'
import accentButton from '@/components/buttons/accentButton.vue'
import axios from 'axios'

export default {
    name: 'TopSearchBar',
    components: {
        headerSearch,
        accentButton,
    },
    data() {
        return {
            buttons: [
                { title: 'Манга' },
                { title: 'Автор' },
                { title: 'Художник' },
                { title: 'Издатель' },
                { title: 'Пользователь' }
            ],
            previewTextValues: [
                { title: 'Поиск по манге' },
                { title: 'Поиск автора' },
                { title: 'Поиск художника' },
                { title: 'Поиск издателя' },
                { title: 'Поиск пользователя' }
            ],
            selectedIndex: 0,
            text: '', //@app.get("/title/data/{title_id}")
        }
    },
    methods: {
        unselectButton(index) {
            this.selectedIndex = index
            console.log(this.text)
        },
        inputChange() {
            this.text = this.$refs.headerSearchRef.text
            console.log(this.text)
            //console.log(this.getTitlesDataByText(10, 'wqe'))
        },
        search() {
            console.log(this.text)
        }
    }
}
</script>

<template>
    <div class="top-search">
        <headerSearch @input-change="inputChange" ref="headerSearchRef"
            :previewText="previewTextValues[selectedIndex].title" />
        <div ref="search_buttons_row" class="row">
            <accentButton v-for="(button, index) in buttons" :key="index" :class="{ selected: selectedIndex === index }"
                @click="unselectButton(index)" :title="button.title" />
        </div>
        <elementsPreviewMenu />
    </div>
</template>

<style lang="scss">
.top-search {
    position: fixed;
    z-index: 2000;
    width: 100%;
    max-width: 600px;
    left: 50%;
    top: 10px;
    transform: translate(-50%, 0);
    display: flex;
    flex-direction: column;
    gap: 5px;

    .row {
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        gap: 5px;

        * {
            width: 100%;
            padding-right: 4px;
            padding-left: 4px;

            &.selected {
                background-color: var(--inactive-accent-color-active);
                color: var(--selected-font-color);
                padding-right: 8px;
                padding-left: 8px;
            }
        }
    }
}
</style>