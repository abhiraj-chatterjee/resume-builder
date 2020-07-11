$(function () {
    $('button.addName').click(function () {
        $('#newfield').html(`
            <form method="POST" action="/api/technical/update/basic/name">
                <div class="form-group">
                    <label>Name</label>
                    <div class="row">
                        <div class="col">
                            <input type="text" name="name" class="form-control">
                        </div>
                        <div class="col-auto my-1">
                            <button type="submit" class="btn btn-md btn-success">Update</button>
                        </div>
                </div>
            </form>
        `);
        $('button.addName').remove();
    });
    $('button.addEmail').click(function () {
        $('#newfield1').html(`
            <form method="POST" action="/api/technical/update/basic/email">
                <div class="form-group">
                    <label>Email</label>
                    <div class="row">
                        <div class="col">
                            <input type="text" name="email" class="form-control">
                        </div>
                        <div class="col-auto my-1">
                            <button type="submit" class="btn btn-md btn-success">Update</button>
                        </div>
                </div>
            </form>
        `);
        $('button.addEmail').remove();
    });
    $('button.addPhone').click(function () {
        $('#newfield2').html(`
            <form method="POST" action="/api/technical/update/basic/phone">
                <div class="form-group">
                    <label>Phone</label>
                    <div class="row">
                        <div class="col">
                            <input type="text" name="phone" class="form-control">
                        </div>
                        <div class="col-auto my-1">
                            <button type="submit" class="btn btn-md btn-success">Update</button>
                        </div>
                </div>
            </form>
        `);
        $('button.addPhone').remove();
    });
    $('button.addAddress').click(function () {
        $('#newfield3').html(`
            <form method="POST" action="/api/technical/update/basic/address">
                <div class="form-group">
                    <label>Address</label>
                    <div class="row">
                        <div class="col">
                            <input type="text" name="address" class="form-control">
                        </div>
                        <div class="col-auto my-1">
                            <button type="submit" class="btn btn-md btn-success">Update</button>
                        </div>
                </div>
            </form>
        `);
        $('button.addAddress').remove();
    });
    $('button.addLanguage').click(function () {
        $('#newfield4').html(`
            <form method="POST" action="/api/technical/update/lang/none">
                <div class="form-group">
                    <label>Language</label>
                    <div class="row">
                        <div class="col">
                            <input type="text" name="lang" class="form-control">
                        </div>
                        <div class="col-auto my-1">
                            <button type="submit" class="btn btn-md btn-success">Update</button>
                        </div>
                </div>
            </form>
        `);
        $('button.addLanguage').remove();
    });
});
