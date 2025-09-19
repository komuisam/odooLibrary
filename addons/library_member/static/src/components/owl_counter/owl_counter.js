/** @odoo-module **/
import { Component } from "@odoo/owl";

export class OwlCounter extends Component {
  static template = "library_member.OwlCounter";

  onClick() {
    alert(`📚 ¡Este miembro ha prestado ${this.props.count} libros!`);
  }
}
