module ApplicationHelper
#    def logo
#        base_logo = image_tag("logo.png", :alt => "logo", :class => "round")
#        if @logo.nil?
#            base_logo
#        else
#            "#{base_logo}"
#        end
#    end
#
    def title
        base_title = "Ruby on Rails"
        if @title.nil?
            base_title
        else
            "#{base_title} | #{@title}"
        end
    end
end
