const seriesSelect = document.getElementById("seriesSelect");
const subseriesSelect = document.getElementById("subseriesSelect");
const modelSelect = document.getElementById("modelSelect");
const verifyBtn = document.getElementById("verifyBtn");

seriesSelect.addEventListener("change", async () => {
  const series = seriesSelect.value;
  subseriesSelect.innerHTML = '<option value="">Select Subseries</option>';
  modelSelect.innerHTML = '<option value="">Select Model</option>';
  if (!series) return;

  const res = await fetch("/get_subseries", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ series })
  });
  const data = await res.json();
  data.forEach(sub => {
    const opt = document.createElement("option");
    opt.value = sub;
    opt.textContent = sub;
    subseriesSelect.appendChild(opt);
  });
});

subseriesSelect.addEventListener("change", async () => {
  const series = seriesSelect.value;
  const subseries = subseriesSelect.value;
  modelSelect.innerHTML = '<option value="">Select Model</option>';
  if (!subseries) return;

  const res = await fetch("/get_models", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ series, subseries })
  });
  const data = await res.json();
  data.forEach(model => {
    const opt = document.createElement("option");
    opt.value = model;
    opt.textContent = model;
    modelSelect.appendChild(opt);
  });
});

verifyBtn.addEventListener("click", async () => {
  const model = modelSelect.value;
  const cfw = document.getElementById("cfw");
  const cex = document.getElementById("cex");
  const dex = document.getElementById("dex");

  if (!model) {
    cfw.textContent = "—";
    cex.textContent = "—";
    dex.textContent = "—";
    return;
  }

  try {
    const res = await fetch("/check", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ model })
    });
    const data = await res.json();
    cfw.textContent = data.cfw;
    cex.textContent = data.cex;
    dex.textContent = data.dex;
  } catch (err) {
    console.error("Error:", err);
    cfw.textContent = "Error";
    cex.textContent = "Error";
    dex.textContent = "Error";
  }
});
