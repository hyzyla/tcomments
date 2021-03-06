import React, {FC} from 'react'
import {Comment} from '../../types'
import css from './CommentsList.module.css'
import {CommentRow} from "./CommentRow";


interface Props {
    comments: Comment[],
}

export const CommentsList: FC<Props> = ({comments}) => {
    return (
        <>
            <ul className={css.list}>
                {comments.map(comment => {
                    return <CommentRow key={comment.id} comment={comment}/>
                })}
            </ul>
        </>
    );
};
