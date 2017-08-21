import Ember from 'ember';

export default Ember.Component.extend({

  classNames: "nav navbar-nav",

  entered_search: null,
  search: null,
  show_help: true,
  update_entered_search: true,

  init() {
    this._super(...arguments);
    this.set('entered_search', this.get('search'));
  },

  on_entered_search_updated: Ember.observer('search', function() {
    if (this.get('update_entered_search')) {
      this.set('entered_search', this.get('search'));
    }
  }),

  actions: {
    search() {
      let entered_search = this.get("entered_search");
      if (entered_search !== this.get('search')) {
        this.set('searching', true);
      }
      this.set("update_entered_search", false);
      this.set("search", entered_search);
      this.set("update_entered_search", true);
    }
  }
});
