// ==========================================================================
// Project:   Todos.tasksController
// Copyright: ©2011 My Company, Inc.
// ==========================================================================
/*globals Todos */

/** @class

  (Document Your Controller Here)

  @extends SC.ArrayController
*/

Todos.taskController = SC.ObjectController.create(function(){

    var RELATIVE_PATH_TO_FORM = "mainPage.mainPane.middleView.bottomRightView";
    var PATH_TO_FORM = "Todos." + RELATIVE_PATH_TO_FORM;
    var REGEX_MATCH_PROJECT_CODE = /[a-z]{3}-[a-z]{3}/i;

    var loadForm = function() {
        return Todos.getPath(RELATIVE_PATH_TO_FORM);
    }
    var projectCodeText = function() {
        return loadForm().get("projectCodeText");
    }   

    return {

    contentBinding: SC.Binding.single('Todos.tasksController.selection'),
    isSaveOk: NO,
    projectCodeMessage: "message goes here",
    isProjectCodeMessageOn: NO,

    saveTask: function() {
        var taskRecord = this.get("content");

        if (this.validateProjectCodeField()) {
            taskRecord.commitRecord();
        } else {
             alert("You must select a task first");
        }
     },
    observeRecordState: function() {
        var taskRecord = this.get("content");
        if (taskRecord.get("status") === SC.Record.READY_DIRTY ||
            taskRecord.get("status") === SC.Record.READY_NEW) {
            this.set("isSaveOk", YES);
        } else {
            this.set("isSaveOk", NO); 
        }
        this.clearValidationMessages();
        }.observes("*content.status"),

        clearValidationMessages: function() {
            this.set("projectCodeMessage", "");
            this.set("isProjectCodeMessageOn", NO);
        },

        validateProjectCodeField: function() {
            var taskRecord = this.get("content");
            if (!taskRecord) {
                return YES;
            }
            var projectCode = taskRecord.get("projectCode");
            if (projectCode) {
                if (!projectCode.match(REGEX_MATCH_PROJECT_CODE)) {
                    this.set("projectCodeMessage", "invalid project code: must be 3 letters dash 3 letters");
                    this.set("isProjectCodeMessageOn", YES);
                                   return NO;              
                } else {
                    this.clearValidationMessages();
                    return YES;
                }
            }else {
                  return YES;
            }      
        },
        observeProjectCodeKeyResponder: function() {
            var component = projectCodeText();
            if (component.get("isKeyResponder")==NO) {
                this.validateProjectCodeField();
            }
        }.observes(PATH_TO_FORM + ".projectCodeText.isKeyResponder"),
    }}());

//});
Todos.tasksController = SC.ArrayController.create(
   SC.CollectionViewDelegate,
        /** @scope Todos.tasksController.prototype */ {
    summary: function(){
     var len = this.get('length'), ret ;

     if (len  && len > 0){
        ret = len === 1 ? "1 task" : "%@ tasks".fmt(len) ;
        }else
        ret = "No tasks";

        return ret;
    }.property('length').cacheable(),

    collectionViewDeleteContent: function(view, content, indexes) {
        var records = indexes.map(function(idx) {
            return this.objectAt(idx);
        }, this);
        records.invoke('destroy');

        var selIndex = indexes.get('min')-1;
        if (selIndex<0) selIndex = 0;
        this.selectObject(this.objectAt(selIndex));
    },
    addTask: function() {
        var task;
        task = Todos.store.createRecord(Todos.Task, {
                "description": "New Task",
                "isDone": false
        });
        this.selectObject(task);
        this.invokeLater(function() {
                var contentIndex = this.indexOf(task);
                var list = Todos.mainPage.getPath('mainPane.middleView.topLeftView.contentView')
                var listItem = list.itemViewForContentIndex(contentIndex);
                listItem.beginEditing();
            });
            return YES;
          },
    toggleDone: function() {
        var sel = this.get('selection');
        sel.setEach('isDone', !sel.everyProperty('isDone'));
        return YES;
    }
}) ;
