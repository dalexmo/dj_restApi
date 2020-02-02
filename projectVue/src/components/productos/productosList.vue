<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado de Productos</h2>

                <div class="col-md-12">
                    <b-table stipped hover :items="productos" :field="fields">
                        
                    </b-table>
                </div>
            </div>
        </div>
    </div>    
</template>
<script>
export default {
    data () {
        return {
            fields: [
                {key: 'title', label: 'Titulo'},
                {key: 'description', label: 'Descripción'},
                {key: 'action', label: 'Acción'}
            ],
            productos: []
        }
    }
}
</script>
<style lang="css" scoped>

</style>