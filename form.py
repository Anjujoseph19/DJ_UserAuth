<form>
  <!-- Email input -->
  <div data-mdb-input-init class="form-outline mb-4">
    <input type="email" id="form2Example1" class="form-control" />
    <label class="form-label" for="form2Example1">Email address</label>
  </div>

  <!-- Password input -->
  <div data-mdb-input-init class="form-outline mb-4">
    <input type="password" id="form2Example2" class="form-control" />
    <label class="form-label" for="form2Example2">Password</label>
  </div>

  <!-- 2 column grid layout for inline styling -->
  <div class="row mb-4">
    <div class="col d-flex justify-content-center">
      <!-- Checkbox -->
      <div class="form-check">
        <input class="form-check-input" type="checkbox" value="" id="form2Example31" checked />
        <label class="form-check-label" for="form2Example31"> Remember me </label>
      </div>
    </div>

    <div class="col">
      <!-- Simple link -->
      <a href="#!">Forgot password?</a>
    </div>
  </div>

  <!-- Submit button -->
  <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-block mb-4">Sign in</button>

  <!-- Register buttons -->
  <div class="text-center">
    <p>Not a member? <a href="#!">Register</a></p>
    <p>or sign up with:</p>
    <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
      <i class="fab fa-facebook-f"></i>
    </button>

    <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
      <i class="fab fa-google"></i>
    </button>

    <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
      <i class="fab fa-twitter"></i>
    </button>

    <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-link btn-floating mx-1">
      <i class="fab fa-github"></i>
    </button>
  </div>
</form>



{% block content %}
    <div class="container">
        <form action="#" method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <div class="col-md-8 col-md-offset-2">
                <div class="panel panel-default">
                    <div class="panel-heading">Login</div>
                    <div class="panel-body">
                        {% if error_message %}
                            <p class="bg-danger p-d ml-b">{{ error_message }}</p>
                        {% endif %}

                        <!-- Username input -->
                        <div class="form-group clearfix">
                            <label for="username" class="col-md-4 control-label text-right">Username:</label>
                            <div class="col-md-6">
                                <input name="username" id="username" type="text" class="form-control" required/>
                            </div>
                        </div>

                        <!-- Password input -->
                        <div class="form-group clearfix">
                            <label for="password" class="col-md-4 control-label text-right">Password:</label>
                            <div class="col-md-6">
                                <input type="password" id="password" name="password" class="form-control" required/>
                            </div>
                        </div>

                        <div class="col-md-6 col-md-offset-4">
                            <input name="login" type="submit" onclick = "fun(); value="Login" class="btn btn-success" /> &nbsp;
                            <p>Not a member? <a href="{% url 'register' %}">Register</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>
{% endblock %}