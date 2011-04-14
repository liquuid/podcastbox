class PagesController < ApplicationController
  def home
      @title = "home"
  end

  def help
      @title = "help"
  end

  def contact
      @title = "contact"
  end

  def about
      @title = "about"
  end
end
