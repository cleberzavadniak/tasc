function update_cell(obj, content) {

  if ('html' in content) {
    obj.html(content.html);
  }

  if ('css' in content) {
    for (k in content.css) {
      value = content.css[k];
      obj.css(k, value);
    }
  }

  if ('elements' in content) {
    for (selector in content.elements) {
      html = content.elements[selector];
      obj.children(selector).html(html);
    }
  }
}


function process_message(message) {
  coordinates = message.coordinates;
  selector = "#grid-cell-" + coordinates[0] + "x" + coordinates[1];
  obj = $(selector);

  update_cell(obj, message.content);
}


function process_messages(messages, counter, last_time) {
  for (k in messages) {
    msg = messages[k];
    process_message(msg);
  }

  window.setTimeout(cell_updater, 700, counter + 1, last_time);
}


function cell_updater(counter, last_time) {
  counter = Number(counter);
  if (counter >= 100) {
    counter = 0;
  }

  var date = new Date();
  var time = date.getTime();
  diff = time - last_time;

  data = {counter: counter, time_lapse: diff};

  $.get(SITE_URL + "cells/", data, function(data) {
    process_messages(data.messages, counter, time);
  }).fail(function () {
    window.setTimeout(cell_updater, 1000, counter, last_time);
  });

}


$(document).ready(function () {
  var date = new Date();
  var time = date.getTime();
  cell_updater(0, time);
});
