document.addEventListener('DOMContentLoaded', function () {
    var vacanciesLink = document.getElementById('vacanciesLink');
  
    vacanciesLink.addEventListener('click', function (event) {
      event.preventDefault();
  
      $('#noJobsModal').modal('show');
  
      setTimeout(function() {
        $('#noJobsModal').modal('hide');
      }, 3000);
    });
  });