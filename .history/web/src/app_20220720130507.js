function generatePayment(value) {
    if (value == '') {
        alert('insersci un importo');
        return;
    }
    paypal.Buttons({
        createOrder: function (data, actions) {
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: value
                    }
                }]
            });
        }, onApprove: function (data, actions) {
            alert(data);
            window.open('index.html');

        }
    }).render('#paypal-button-container');


} 
