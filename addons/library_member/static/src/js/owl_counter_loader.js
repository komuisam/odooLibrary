/** @odoo-module **/
import { OwlCounter } from "../components/owl_counter/owl_counter";
import { registry } from "@web/core/registry";
import { useModel } from "@web/model/model";

class OwlCounterWrapper extends OwlCounter {
  setup() {
    super.setup();
    this.model = useModel();
    // Obtiene el valor del campo calculado
    this.count = this.model.root.data.loaned_books_count || 0;
  }

  get props() {
    return {
      count: this.count,
    };
  }
}

registry.category("view_widgets").add("web_owl_counter", {
  component: OwlCounterWrapper,
});
