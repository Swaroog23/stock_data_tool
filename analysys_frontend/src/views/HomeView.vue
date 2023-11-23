<template>
    <div class="home">
        <h1>{{ message }}</h1>
    </div>
</template>

<script lang="ts">
    export default {
        data() {
            return {
                message: "test 1",
            }
        }
    }
</script>

<style>
    .home {
        text-align: center;
        margin-top: 50px;
    }
</style>
