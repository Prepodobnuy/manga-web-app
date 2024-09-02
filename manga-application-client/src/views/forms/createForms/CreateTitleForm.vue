<script>
import fullWidthInput from '@/components/inputs/fullWidthInput.vue';
import oneLineLink from '@/components/links/oneLineLink.vue';
import imageInput from '@/components/inputs/imageInput.vue';
import tagSelect from '@/components/inputs/tagSelect.vue';

export default {
    components: {
        fullWidthInput,
        oneLineLink,
        imageInput,
        tagSelect
    },
    data() {
        return {
            tags: [
                { id: 0, name: "сёнен" },
                { id: 1, name: "романтика" },
                { id: 2, name: "абоба" },
                { id: 3, name: "что то там" },
                { id: 4, name: "рофланы" },
                { id: 5, name: "приколы" },
                { id: 6, name: "угары" },
                { id: 7, name: "что то там" },
                { id: 8, name: "рофланы" },
                { id: 9, name: "приколы" },
                { id: 10, name: "угары" },
                { id: 11, name: "фурри??" }
            ]

        }
    }
}


</script>

<template>
    <div class="ThinViewForm">
        <h4 class="main-h">Создание тайтла</h4>
        <div class="mar-top">
            <h4>Обложка</h4>
            <imageInput :image_width="250" :image_height="350" :width="166" :height="233" />
        </div>
        <div class="mar-top">
            <h4>Оригинальное название</h4>
            <fullWidthInput />
        </div>
        <div class="mar-top">
            <h4>Русское название</h4>
            <fullWidthInput />
        </div>
        <div class="mar-top">
            <h4>Английское название</h4>
            <fullWidthInput />
        </div>
        <div class="mar-top">
            <h4>Альтернативные названия</h4>
            <fullWidthInput previewText="вводите альтернативные названия разделяя символом ' / '" />
        </div>
        <div class="mar-top">
            <tagSelect :tags="tags" title="Жанры" />
        </div>
        <div class="mar-top">
            <tagSelect :tags="tags" title="Тэги" />
        </div>
        <div class="mar-top">
            <h4>Автор <span class="right">
                    <oneLineLink text="добавить нового автора" link="/create/author" />
                </span></h4>
            <fullWidthInput />
        </div>
        <div class="mar-top">
            <h4>Художник <span class="right">
                    <oneLineLink text="добавить нового художника" link="/create/artist" />
                </span></h4>
            <fullWidthInput />
        </div>
        <div class="mar-top">
            <h4>Издатель <span class="right">
                    <oneLineLink text="добавить нового издателя" link="/create/publisher" />
                </span></h4>
            <fullWidthInput />
        </div>
    </div>
</template>


<style lang="scss" scoped>
.mar-top {
    margin-top: 30px;

    h4 {
        position: relative;
        margin-bottom: 8px;
        display: flex;
        flex-wrap: nowrap;

        .right {
            position: absolute;
            right: 0;
            font-size: medium;
        }
    }
}
</style>