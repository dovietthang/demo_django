<template>
    <div class="product-from">
        <div class="container">
            <div class="text-start">
                <h3 class="mt-5 mb-2"> Form product </h3>
                <div class="my-3 ">
                    <router-link class="btn btn-secondary" to="/product">Back</router-link>
                </div>
            </div>
            <form>
                <div class="mb-3">
                    <label for="formGroupExampleInput" class="form-label">Example label</label>
                    <input type="text" class="form-control" id="formGroupExampleInput"
                        placeholder="Example input placeholder">
                </div>
                <div class="mb-3">
                    <label for="formGroupExampleInput2" class="form-label">Another label</label>
                    <input type="text" class="form-control" id="formGroupExampleInput2"
                        placeholder="Another input placeholder">
                </div>
                <div class="row mb-3">
                    <div class="col">
                        <label for="formGroupExampleInput2" class="form-label">Another label</label>
                        <input type="text" class="form-control" placeholder="First name" aria-label="First name">
                    </div>
                    <div class="col">
                        <label for="formGroupExampleInput2" class="form-label">Another label</label>

                        <input type="text" class="form-control" placeholder="Last name" aria-label="Last name">
                    </div>
                </div>
                <div class="mb-3">
                    <label for="formGroupExampleInput2" class="form-label">Another label</label>
                    <input type="text" class="form-control" id="formGroupExampleInput2"
                        placeholder="Another input placeholder">
                </div>
                
                <button type="submit" class="btn btn-primary">submit</button>

            </form>
        </div>

    </div>
</template>