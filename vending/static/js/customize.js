document.addEventListener("DOMContentLoaded", () => {
  const teaQty = document.getElementById("teaQty");
  const milkQty = document.getElementById("milkQty");
  const sugarQty = document.getElementById("sugarQty");
  const costDisplay = document.getElementById("costDisplay");
  const paymentInput = document.getElementById("paymentInput");
  const changeDisplay = document.getElementById("changeDisplay");
  const payButton = document.getElementById("payButton");
  const form = document.getElementById("customizeForm");

  const teaError = document.getElementById("teaError");
  const milkError = document.getElementById("milkError");
  const sugarError = document.getElementById("sugarError");

  function validate() {
    let valid = true;
    teaError.textContent = "";
    milkError.textContent = "";
    sugarError.textContent = "";

    if (parseFloat(teaQty.value) > stock.tea) {
      teaError.textContent = `Max: ${stock.tea}g`;
      valid = false;
    }
    if (parseFloat(milkQty.value) > stock.milk) {
      milkError.textContent = `Max: ${stock.milk}ml`;
      valid = false;
    }
    if (parseFloat(sugarQty.value) > stock.sugar) {
      sugarError.textContent = `Max: ${stock.sugar}g`;
      valid = false;
    }
    return valid;
  }

  function calculateCost() {
    const tea = parseFloat(teaQty.value) || 0;
    const milk = parseFloat(milkQty.value) || 0;
    const sugar = parseFloat(sugarQty.value) || 0;
    return tea * prices.tea + milk * prices.milk + sugar * prices.sugar;
  }

  function updateCost() {
    if (validate()) {
      const cost = calculateCost();
      costDisplay.textContent = `Total Cost: $${cost.toFixed(2)}`;
      payButton.disabled = false;
      changeDisplay.textContent = "";
    } else {
      costDisplay.textContent = "Total Cost: -";
      payButton.disabled = true;
      changeDisplay.textContent = "";
    }
  }

  [teaQty, milkQty, sugarQty].forEach((el) =>
    el.addEventListener("input", updateCost)
  );
  updateCost();

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (!validate()) return;

    const cost = calculateCost();
    const paymentStr = paymentInput.value.trim();
    const payments = paymentStr
      .split(",")
      .map((s) => parseFloat(s))
      .filter((n) => !isNaN(n));
    const totalPaid = payments.reduce((a, b) => a + b, 0);

    if (totalPaid < cost) {
      changeDisplay.textContent = `Insufficient! You need $${(
        cost - totalPaid
      ).toFixed(2)} more.`;
    } else {
      const change = totalPaid - cost;
      changeDisplay.textContent = `Payment accepted! Change: $${change.toFixed(
        2
      )}.`;
    }
  });
});
