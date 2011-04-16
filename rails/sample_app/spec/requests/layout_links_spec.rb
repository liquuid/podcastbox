require 'spec_helper'

describe "LayoutLinks" do
  it "should have a home page at '/'" do
    get "/"
    response.should have_selector('title', :content => "Ruby on Rails | home")
  end
  
  it "should have a contact page at '/contact'" do
    get "/contact"
    response.should have_selector('title', :content => "Ruby on Rails | contact")
  end
  
  it "should have a aboutpage at '/about'" do
    get "/about"
    response.should have_selector('title', :content => "Ruby on Rails | about")
  end
  
  it "should have a help page at '/help'" do
    get "/help"
    response.should have_selector('title', :content => "Ruby on Rails | help")
  end
  it "should have a signup page at '/signup'" do
    get "/signup"
    response.should have_selector('title', :content => "Sign up")
  end

end
