// https://materializecss.com/navbar.html
// Original snippet:
// document.addEventListener('DOMContentLoaded', function () {
//   var elems = document.querySelectorAll('.sidenav');
//   var instances = M.Sidenav.init(elems, options);
// });

document.addEventListener('DOMContentLoaded', function () {
  // sidenav initialization
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // datepicker init

  // Original snippet:
  // https://materializecss.com/pickers.html
  // document.addEventListener('DOMContentLoaded', function() {
  //   var elems = document.querySelectorAll('.datepicker');
  //   var instances = M.Datepicker.init(elems, options);
  // });

  // See above link for guide on setting options
  let datepicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    // Internationalization options. Set them with this object
    i18n: {
      done: "Select"
    }
  });

  // Form select init
  let selects = document.querySelectorAll('select');
  M.FormSelect.init(selects);
});