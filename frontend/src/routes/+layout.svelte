<script lang="ts">
    import "./app.css";
</script>

<main class="wrapper">
    <slot></slot>
</main>

<style>
    .wrapper {
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>