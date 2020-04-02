window.onload = function () {
  axios.interceptors.request.use((config) => {
    // Do something before request is sent
    alert('kjn');
    return config;
  }, function (error) {
    // Do something with request error
    return Promise.reject(error);
  });
};
