import {Component} from "solid-js";
import style from "./UserPage.module.css";

const UserPage: Component = (): any => {
    return (
        <div class={style["main-container"]}>
            <div class="upper-zone">
                <h1>Upper zone</h1>
            </div>
            <div class={style["lower-zone"]}>
                <h1>Lower zone</h1>
            </div>

            {/*{% if page_obj.has_other_pages %}*/}
            {/*<div class="pagination">*/}
            {/*    {% if page_obj.has_previous %}*/}
            {/*    <a href="?page=1">&laquo; first</a>*/}
            {/*    <a href="?page={{ page_obj.previous_page_number }}">previous</a>*/}
            {/*    {% endif %}*/}

            {/*    {% for num in page_obj.paginator.page_range %}*/}
            {/*    {% if page_obj.number == num %}*/}
            {/*    <span class="current">{{ num }}</span>*/}
            {/*    {% elif num > page_obj.number|add:-3 and num < page_obj.number|add:3 %}*/}
            {/*    <a href="?page={{ num }}">{{ num }}</a>*/}
            {/*    {% endif %}*/}
            {/*    {% endfor %}*/}

            {/*    {% if page_obj.has_next %}*/}
            {/*    <a href="?page={{ page_obj.next_page_number }}">next</a>*/}
            {/*    <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>*/}
            {/*    {% endif %}*/}
            {/*</div>*/}
            {/*{% endif %}*/}
        </div>

    )
}

export default UserPage;
