const item1 = document.querySelector(".item-1");
const item2 = document.querySelector(".item-2");
const item3 = document.querySelector(".item-3");
let sales = 0;
let visitors = 0;
let AvgAmount = 0;
item1.addEventListener("click", () => {
    salesToday().then((data) => {
        sales = data;
        item1.innerHTML = `<i class="fas fa-store fa-3x"></i>
                           <h1>Rs ${data.toString()}</h1>
                           <p>Today's Sales</p>
                           <br>`
    });
});

item2.addEventListener("click", () => {
    uniqueVisitors().then((data) => {
        visitors = data;
        item2.innerHTML = `<i class="fas fa-flag fa-3x"></i>
        <h1>${data} </h1>
        <p>Unique Customers</p>`
    });
});

item3.addEventListener("click", () => {
    AvgAmount = ((Math.round(sales / visitors) * 100) / 100).toFixed(2);
    console.log(AvgAmount);
    item3.innerHTML = `<i class="fas fa-coins fa-3x"></i>
    <h1>Rs ${AvgAmount} </h1>
    <p>Average amount spent</p>
    <br>`

});

