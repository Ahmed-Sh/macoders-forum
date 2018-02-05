(function(window, undefined) {
  var dictionary = {
    "1dfa48e9-225a-4db4-83d6-467a7fce701a": "add_topic",
    "eb270a93-43d6-464d-8cd8-9ebce35a0234": "members",
    "e4341931-208b-4d2e-b953-915bb202134a": "about_us",
    "9dcc54d6-2070-4bb9-a5a3-139884f0e64f": "user_profile",
    "f5ba6248-49b9-4cbc-8f8f-39474d506b8d": "topic",
    "d12245cc-1680-458d-89dd-4f0d7fb22724": "home",
    "87db3cf7-6bd4-40c3-b29c-45680fb11462": "960 grid - 16 columns",
    "e5f958a4-53ae-426e-8c05-2f7d8e00b762": "960 grid - 12 columns",
    "f39803f7-df02-4169-93eb-7547fb8c961a": "Template 1",
    "d7df6e36-6b19-429b-ae85-d9e9c8958638": "main_layout",
    "bb8abf58-f55e-472d-af05-a7d1bb0cc014": "default"
  };

  var uriRE = /^(\/#)?(screens|templates|masters|scenarios)\/(.*)(\.html)?/;
  window.lookUpURL = function(fragment) {
    var matches = uriRE.exec(fragment || "") || [],
        folder = matches[2] || "",
        canvas = matches[3] || "",
        name, url;
    if(dictionary.hasOwnProperty(canvas)) { /* search by name */
      url = folder + "/" + canvas;
    }
    return url;
  };

  window.lookUpName = function(fragment) {
    var matches = uriRE.exec(fragment || "") || [],
        folder = matches[2] || "",
        canvas = matches[3] || "",
        name, canvasName;
    if(dictionary.hasOwnProperty(canvas)) { /* search by name */
      canvasName = dictionary[canvas];
    }
    return canvasName;
  };
})(window);