document.addEventListener('DOMContentLoaded', function() {
  function attachCalendarLinks() {
    document.querySelectorAll('#calendar-zone a').forEach(function(link) {
      link.addEventListener('click', calendarClickHandler);
    });
  }

  function calendarClickHandler(e) {
    e.preventDefault();
    fetch(this.href)
      .then(response => response.text())
      .then(html => {
        document.getElementById('calendar-zone').innerHTML = html;
        attachCalendarLinks(); // Ré-attache proprement les événements
      });
  }

  attachCalendarLinks();
});